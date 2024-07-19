import logging

logger = logging.getLogger(__name__)

class ContextMatcher:
    def find_context_lines(self, lines, start_context, end_context):
        logger.debug(f"Searching for start context: '{start_context}'")
        start_line = self._find_start_context(lines, start_context)
        
        logger.debug(f"Start context found at line {start_line}")
        
        if start_line is None:
            logger.error("Couldn't find matching start context")
            return None, None
        
        if end_context:
            logger.debug(f"Searching for end context: '{end_context}'")
            end_line = self._find_end_context(lines[start_line:], end_context)
            if end_line is None:
                logger.error("Couldn't find matching end context")
                return start_line, None
            end_line += start_line  # Adjust end_line to be relative to the whole file
        else:
            end_line = None
        
        logger.debug(f"End context found at line {end_line}")
        
        return start_line, end_line

    def _find_start_context(self, lines, context):
        if not context:
            logger.debug("No start context provided, assuming beginning of file")
            return 0  # If no start context is provided, assume the beginning of the file
        
        context_lines = context.strip().split('\n')
        for i in range(len(lines) - len(context_lines) + 1):
            if all(lines[i + j].strip() == context_lines[j].strip() for j in range(len(context_lines))):
                logger.debug(f"Found start context at line {i}")
                return i  # Return the first line of the context
        logger.debug("Start context not found")
        return None

    def _find_end_context(self, lines, context):
        if not context:
            logger.debug("No end context provided")
            return None  # If no end context is provided, return None
        
        context_lines = context.strip().split('\n')
        for i in range(len(lines) - len(context_lines) + 1):
            if all(lines[i + j].strip() == context_lines[j].strip() for j in range(len(context_lines))):
                logger.debug(f"Found end context at line {i + len(context_lines) - 1}")
                return i + len(context_lines) - 1  # Return the last line of the context
        logger.debug("End context not found")
        return None