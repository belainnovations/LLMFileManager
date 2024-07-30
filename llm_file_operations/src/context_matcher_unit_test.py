import pytest
from context_matcher import ContextMatcher

@pytest.fixture
def context_matcher():
    return ContextMatcher()

def test_initialization(context_matcher):
    assert isinstance(context_matcher, ContextMatcher)

def test_find_context_lines_valid_contexts(context_matcher):
    lines = ["line1", "line2", "start", "middle", "end", "line6"]
    start, end = context_matcher.find_context_lines(lines, "start", "end")
    assert start == 2
    assert end == 4

def test_find_context_lines_start_only(context_matcher):
    lines = ["line1", "line2", "start", "middle", "end", "line6"]
    start, end = context_matcher.find_context_lines(lines, "start", None)
    assert start == 2
    assert end is None

def test_find_context_lines_no_contexts(context_matcher):
    lines = ["line1", "line2", "line3"]
    start, end = context_matcher.find_context_lines(lines, None, None)
    assert start == 0
    assert end is None

def test_find_context_lines_start_not_found(context_matcher):
    lines = ["line1", "line2", "line3"]
    start, end = context_matcher.find_context_lines(lines, "nonexistent", "line3")
    assert start is None
    assert end is None

def test_find_context_lines_end_not_found(context_matcher):
    lines = ["line1", "line2", "line3"]
    start, end = context_matcher.find_context_lines(lines, "line1", "nonexistent")
    assert start == 0
    assert end is None

def test_find_context_lines_multiline_contexts(context_matcher):
    lines = ["line1", "start1", "start2", "middle", "end1", "end2", "line7"]
    start, end = context_matcher.find_context_lines(lines, "start1\nstart2", "end1\nend2")
    assert start == 1
    assert end == 5

def test_find_context_lines_beginning_of_file(context_matcher):
    lines = ["start", "middle", "end", "line4"]
    start, end = context_matcher.find_context_lines(lines, "start", "end")
    assert start == 0
    assert end == 2

def test_find_context_lines_end_of_file(context_matcher):
    lines = ["line1", "start", "middle", "end"]
    start, end = context_matcher.find_context_lines(lines, "start", "end")
    assert start == 1
    assert end == 3

def test_find_context_lines_identical_contexts(context_matcher):
    lines = ["line1", "same", "line3", "same", "line5"]
    start, end = context_matcher.find_context_lines(lines, "same", "same")
    assert start == 1
    assert end == 3

def test_find_context_lines_overlapping_contexts(context_matcher):
    lines = ["line1", "overlap1", "overlap2", "line4"]
    start, end = context_matcher.find_context_lines(lines, "overlap1\noverlap2", "overlap2")
    assert start == 1
    assert end == 2

def test_find_start_context(context_matcher):
    lines = ["line1", "start", "line3"]
    start = context_matcher._find_start_context(lines, "start")
    assert start == 1

def test_find_end_context(context_matcher):
    lines = ["line1", "end", "line3"]
    end = context_matcher._find_end_context(lines, "end")
    assert end == 1

def test_whitespace_handling(context_matcher):
    lines = ["line1", "  start  ", "line3", "  end  ", "line5"]
    start, end = context_matcher.find_context_lines(lines, "start", "end")
    assert start == 1
    assert end == 3

@pytest.mark.parametrize("file_size", [100, 1000, 10000])
def test_performance_large_files(context_matcher, file_size):
    lines = [f"line{i}" for i in range(file_size)]
    lines[file_size // 2] = "start"
    lines[-2] = "end"
    start, end = context_matcher.find_context_lines(lines, "start", "end")
    assert start == file_size // 2
    assert end == file_size - 2
