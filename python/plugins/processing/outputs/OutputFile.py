# -*- coding: utf-8 -*-

"""
***************************************************************************
    OutputFile.py
    ---------------------
    Date                 : August 2012
    Copyright            : (C) 2012 by Victor Olaya
    Email                : volayaf at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Victor Olaya'
__date__ = 'August 2012'
__copyright__ = '(C) 2012, Victor Olaya'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from processing.outputs.Output import Output


class OutputFile(Output):

    def __init__(self, name='', description='', ext = None):
        self.name = name
        self.description = description
        self.ext = ext

    def getFileFilter(self, alg):
        if self.ext is None:
            return 'All files(*.*)'
        else:
            return '%s files(*.%s)' % self.ext

    def getDefaultFileExtension(self, alg):
        return self.ext or 'file'
