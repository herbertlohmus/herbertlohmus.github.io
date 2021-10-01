def compile_headers(line):
    '''
    Convert markdown headers into <h1>,<h2>,etc tags.
    HINT:
    This is the simplest function to implement in this assignment.
    Use a slices to extract the first part of the line,
    then use if statements to check if they match the appropriate header markdown commands.
    >>> compile_headers('# This is the main header')
    '<h1> This is the main header</h1>'
    >>> compile_headers('## This is a sub-header')
    '<h2> This is a sub-header</h2>'
    >>> compile_headers('### This is a sub-header')
    '<h3> This is a sub-header</h3>'
    >>> compile_headers('#### This is a sub-header')
    '<h4> This is a sub-header</h4>'
    >>> compile_headers('##### This is a sub-header')
    '<h5> This is a sub-header</h5>'
    >>> compile_headers('###### This is a sub-header')
    '<h6> This is a sub-header</h6>'
    >>> compile_headers('      # this is not a header')
    '      # this is not a header'
    '''
    if line[0:6] == '######':
        line = '<h6>' + line[6:] + '</h6>'
    if line[0:5] == '#####':
        line = '<h5>' + line[5:] + '</h5>'
    if line[0:4] == '####':
        line = '<h4>' + line[4:] + '</h4>'
    if line[0:3] == '###':
        line = '<h3>' + line[3:] + '</h3>'
    if line[0:2] == '##':
        line = '<h2>' + line[2:] + '</h2>'
    if line[0] == '#':
        line = '<h1>' + line[1:] + '</h1>'

    return line


def compile_italic_star(line):
    '''
    Convert "*italic*" into "<i>italic</i>".
    HINT:
    Italics require carefully tracking the beginning and ending positions of the text to be replaced.
    This is similar to the `delete_HTML` function that we implemented in class.
    It's a tiny bit more complicated since we are not just deleting substrings from the text,
    but also adding replacement substrings.
    >>> compile_italic_star('*This is italic!* This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_star('*This is italic!*')
    '<i>This is italic!</i>'
    >>> compile_italic_star('This is *italic*!')
    'This is <i>italic</i>!'
    >>> compile_italic_star('This is not *italic!')
    'This is not *italic!'
    >>> compile_italic_star('*')
    '*'
    '''
    start_index = None
    stop_index = None
    for i in range(len(line)):
        if line[i] == '*':
            if start_index is None:
                start_index = i
            else:
                stop_index = i

    if start_index is not None and stop_index is not None:
        new_line = line[:start_index] + '<i>' + line[start_index +
                                                     1:stop_index] + '</i>' + line[stop_index+1:]
    else:
        new_line = line

    return new_line


def compile_italic_underscore(line):
    '''
    Convert "_italic_" into "<i>italic</i>".
    HINT:
    This function is almost exactly the same as `compile_italic_star`.
    >>> compile_italic_underscore('_This is italic!_ This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_underscore('_This is italic!_')
    '<i>This is italic!</i>'
    >>> compile_italic_underscore('This is _italic_!')
    'This is <i>italic</i>!'
    >>> compile_italic_underscore('This is not _italic!')
    'This is not _italic!'
    >>> compile_italic_underscore('_')
    '_'
    '''
    start_index = None
    stop_index = None
    for i in range(len(line)):
        if line[i] == '_':
            if start_index is None:
                start_index = i
            else:
                stop_index = i

    if start_index is not None and stop_index is not None:
        new_line = line[:start_index] + '<i>' + line[start_index +
                                                     1:stop_index] + '</i>' + line[stop_index+1:]
    else:
        new_line = line

    return new_line
