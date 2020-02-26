"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.
      Returns IDENTICAL if the two lines are the same.
    """
    
    # finds the minimum length
    min_len = min(len(line1), len(line2))
    # for all the indexes in min_len
    for idx in range(min_len):    
        if line1[idx] != line2[idx]:
            # finds out the idx of the 1st difference
            return idx    
    if len(line1) != len(line2):
        # reached min_len and the the idx were length differs
        return min_len
    # passed everything so they are identical
    return IDENTICAL    

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    
    # calculates the minimum length
    min_len = min(len(line1), len(line2))
    # a newline /n or return /r is found 
    # also an erroneus index value like
    # negative or bigger than the length
    if ("\n" in line1 or "\n" in line2) or \
        ("\r" in line1 or "\r" in line2):
        return ""
    if  (idx < 0 or idx > min_len):
        return ""
    # returns the 3 lines
    return line1 + "\n" + "="*idx+ "^" + "\n" + line2 + "\n"    

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.
      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    
    # finds de minimum length
    min_len = min(len(lines1), len(lines2))  
    # for every line in the range
    for lin in range(min_len):
        # assigns lines1 to line1 idx by idx
        line1 = lines1[lin]
        # assigns lines2 to line2 idx by idx
        line2 = lines2[lin]
        # finds the difference
        idx = singleline_diff(line1, line2)
        # if lin & idx are >= 0
        if lin >= 0 and idx >= 0:
            # returns lin and idx
            return (lin, idx)
    # different length
    if len(lines1) != len(lines2):    
        return (min_len, 0)
    # no differences
    return (IDENTICAL, IDENTICAL)    

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    
    # define the empty list of lines
    lines = []
    # opens the file
    file = open(filename, "rt")
    # for every line in the file
    for line in file:
        # replace new lines if any
        line = line.replace("\n", "")
        # replace returns if any
        line = line.replace("\r", "")
        # appends the line
        lines.append(line)
    # closes the file
    file.close()
    # returns the list of lines
    return lines    

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """

    # assigns filename1 lines to lines1
    lines1 = get_file_lines(filename1)
    # assigns filename2 lines to lines2
    lines2 = get_file_lines(filename2)
    # assigns to linidx the line & idx from multile_diff
    linidx = multiline_diff(lines1, lines2)
    # if there a difference returns the 4 lines with info
  
    if linidx[0] != -1 and linidx[1] != -1:
        # if the file containing lines1 is empty
        if len(lines1) == 0:
            return "Line 0:" + "\n" + \
            singleline_diff_format("", lines2[0], 0)
        # if the file containing lines2 is empty
        if len(lines2) == 0:
            return "Line 0:" + "\n" + \
            singleline_diff_format(lines1[0], "", 0)
        # if the files are not empty then program performs the verifiations
        return "Line " + str(linidx[0]) + ":" + "\n" + \
        singleline_diff_format(lines1[linidx[0]], lines2[linidx[0]], linidx[1])
    # if there is no difference
    return "No differences\n"
