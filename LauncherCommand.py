# -*- coding: utf-8 -*-
"""
    Launcher Command module
    Implements the command:
    launcher -t U1709 -load TestProgram.una -sim simname -qual -nodisplay
"""
import subprocess


class LauncherCommand:
    def __init__(self, unisonrelease, testprogramname, simname, tpra=False):
        self.commandList = []
        self.unisonrelease = unisonrelease
        self.testprogramname = testprogramname
        self.simname = simname
        self.qualOS = tpra
        if tpra:
            self.qualOS = True
        self.createCommand()

    def createCommand(self):
        print self.unisonrelease
        self.commandList.append("launcher")
        self.commandList.append("-t")
        self.commandList.append(self.unisonrelease)
        self.commandList.append("-load")
        self.commandList.append(self.testprogramname)
        self.commandList.append("-sim")
        self.commandList.append(self.simname)
        if self.qualOS:
            self.commandList.append("-qual")
        self.commandList.append("-nodisplay")

    def runCommand(self):
        process = subprocess.Popen(self.commandList, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
