# -*- coding: utf-8 -*- 

"""
***************************************************************************
    Csv2Grid.py
    ---------------------
    Date                 : June 2014
    Copyright            : (C) 2014 by Agresta S. Coop
    Email                : iescamochero at agresta dot org
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Agresta S. Coop - www.agresta.org'
__date__ = 'June 2014'
__copyright__ = '(C) 2014, Agresta S. Coop'
# This will get replaced with a git SHA1 when you do a git archive
__revision__ = '$Format:%H$'

import os
import subprocess
from PyQt4 import QtGui
from processing.parameters.ParameterFile import ParameterFile
from processing.parameters.ParameterString import ParameterString
from processing.outputs.OutputFile import OutputFile
from processing.lidar.fusion.FusionAlgorithm import FusionAlgorithm
from processing.lidar.fusion.FusionUtils import FusionUtils


class Csv2Grid(FusionAlgorithm):

    INPUT = 'INPUT'
    COLUMN = 'COLUMN'
    OUTPUT = 'OUTPUT'

    def defineCharacteristics(self):
        self.name = 'Csv2Grid'
        self.group = 'Points'
        self.addParameter(ParameterFile(self.INPUT, 'CSV Files'))
        self.addParameter(ParameterString(self.COLUMN, 'Column'))
        self.addOutput(OutputFile(self.OUTPUT, 'Raster Output file'))


    def processAlgorithm(self, progress):
        commands = [os.path.join(FusionUtils.FusionPath(), 'CSV2Grid.exe')]
        commands.append('/verbose')
        files = self.getParameterValue(self.INPUT).split(';')
        if len(files) == 1:
            commands.append(self.getParameterValue(self.INPUT))
        else:
            FusionUtils.createFileList(files)
            commands.append(FusionUtils.tempFileListFilepath())
        commands.append(self.getParameterValue(self.COLUMN))
        commands.append(self.getOutputValue(self.OUTPUT) + '.asc')
        FusionUtils.runFusion(commands, progress)
