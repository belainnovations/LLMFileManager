import os
import logging

logger = logging.getLogger(__name__)

class FileOperator:
    def __init__(self, context_matcher, error_handler):
        self.context_matcher = context_matcher
        self.error_handler = error_handler

    def execute(self, instruction):
        logger.debug(f"Executing instruction: {instruction}")
        action = instruction.get('action')
        file_path = instruction.get('file')

        logger.debug(f"Action: {action}, File: {file_path}")

        if not file_path:
            return self.error_handler.handle_error("Missing 'file' in instruction")

        if not action:
            return self.error_handler.handle_error("Missing 'action' in instruction")

        if action.upper() == 'CREATE_FILE':
            return self.create_file(file_path, instruction.get('code', ''))
        elif action.upper() == 'CREATE_FOLDER':
            return self.create_folder(file_path)
        elif action.upper() == 'DELETE_FILE':
            return self.delete_file(file_path)
        elif action.upper() == 'DELETE_FOLDER':
            return self.delete_folder(file_path)
        elif action.upper() in ['REPLACE', 'INSERT', 'DELETE']:
            return self.modify_file(file_path, action.upper(), instruction)
        else:
            return self.error_handler.handle_error(f"Unknown action: {action}")

    def create_file(self, file_path, content):
        try:
            dir_path = os.path.dirname(file_path)
            if dir_path and not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)

            content = content if content is not None else ''

            with open(file_path, 'w', newline='') as f:
                f.write(content)

            logger.info(f"Created file: {file_path}")
            return f"Created file: {file_path}"
        except Exception as e:
            error_msg = f"Error creating file: {str(e)}"
            logger.error(error_msg, exc_info=True)
            return self.error_handler.handle_error(error_msg)

    def create_folder(self, folder_path):
        try:
            os.makedirs(folder_path, exist_ok=True)
            logger.info(f"Created folder: {folder_path}")
            return f"Created folder: {folder_path}"
        except Exception as e:
            error_msg = f"Error creating folder: {str(e)}"
            logger.error(error_msg, exc_info=True)
            return self.error_handler.handle_error(error_msg)

    def delete_file(self, file_path):
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                logger.info(f"Deleted file: {file_path}")
                return f"Deleted file: {file_path}"
            except Exception as e:
                error_msg = f"Error deleting file: {str(e)}"
                logger.error(error_msg, exc_info=True)
                return self.error_handler.handle_error(error_msg)
        else:
            return self.error_handler.handle_error(f"File not found: {file_path}")

    def delete_folder(self, folder_path):
        if os.path.exists(folder_path):
            try:
                shutil.rmtree(folder_path)
                logger.info(f"Deleted folder: {folder_path}")
                return f"Deleted folder: {folder_path}"
            except Exception as e:
                error_msg = f"Error deleting folder: {str(e)}"
                logger.error(error_msg, exc_info=True)
                return self.error_handler.handle_error(error_msg)
        else:
            return self.error_handler.handle_error(f"Folder not found: {folder_path}")

    def modify_file(self, file_path, action, instruction):
        try:
            with open(file_path, 'r', newline='') as f:
                lines = f.readlines()

            start_context = instruction.get('start_context', '')
            end_context = instruction.get('end_context', '')

            logger.debug(f"Start context: {start_context}")
            logger.debug(f"End context: {end_context}")

            start_line, end_line = self.context_matcher.find_context_lines(lines, start_context, end_context)

            logger.debug(f"Found start line: {start_line}")
            logger.debug(f"Found end line: {end_line}")

            if start_line is None:
                return self.error_handler.handle_error("Couldn't find matching start context")

            if action in ['INSERT', 'REPLACE']:
                new_code = instruction.get('code', '')
                logger.debug(f"New code to insert/replace: {new_code}")

                base_indent = self._get_indent(lines[start_line])
                logger.debug(f"Base indent: '{base_indent}'")

                adjusted_code = self._adjust_indent(new_code, base_indent)
                logger.debug(f"Adjusted code: {adjusted_code}")

                if action == 'INSERT':
                    logger.debug(f"Inserting at line: {start_line}")
                    lines = lines[:start_line] + adjusted_code.splitlines(True) + lines[start_line:]
                else:  # REPLACE
                    if end_line is None:
                        return self.error_handler.handle_error("Couldn't find end context for REPLACE")
                    logger.debug(f"Replacing lines {start_line} to {end_line}")
                    lines = lines[:start_line] + adjusted_code.splitlines(True) + lines[end_line + 1:]
            elif action == 'DELETE':
                if end_line is None:
                    return self.error_handler.handle_error("Couldn't find end context for DELETE")
                logger.debug(f"Deleting lines {start_line} to {end_line}")
                lines = lines[:start_line] + lines[end_line + 1:]

            logger.debug(f"Modified lines: {lines}")

            with open(file_path, 'w', newline='') as f:
                f.writelines(lines)

            logger.info(f"Successfully performed {action} operation on {file_path}")
            return f"Successfully performed {action} operation on {file_path}"
        except Exception as e:
            error_msg = f"Error modifying file: {str(e)}"
            logger.error(error_msg, exc_info=True)
            return self.error_handler.handle_error(error_msg)

    def _get_indent(self, line):
        indent = line[:len(line) - len(line.lstrip())]
        logger.debug(f"Detected indent: '{indent}'")
        return indent

    def _adjust_indent(self, code, base_indent):
        logger.debug(f"Adjusting indent. Base indent: '{base_indent}'")
        lines = code.splitlines()
        adjusted_lines = []
        
        for line in lines:
            if line.strip():
                adjusted_line = base_indent + line
                logger.debug(f"Adjusted line: '{adjusted_line.rstrip()}'")
                adjusted_lines.append(adjusted_line)
            else:
                adjusted_lines.append(base_indent)
                logger.debug("Preserved empty line")
        
        return '\n'.join(adjusted_lines) + '\n'