from sikuli import *
from _uimap import *
from xmlrunner import *
import HTMLTestRunner
import math
import os
bdLibPath = os.path.abspath(sys.argv[0] + "..")
if not bdLibPath in sys.path: sys.path.append(bdLibPath)


def RunBrowserToUrl(browser,toUrl):
    #TestAction("Start " +browser +" "+toUrl)
    sleep(0.5)
    type("d",KEY_WIN); sleep(1)
    type("r", KEY_WIN); sleep(1)
    type(browser+" "); sleep(1)
    type(toUrl); sleep(1)
    type(Key.ENTER)

def StartApp(appName):
    sleep(1)
    type("d",KEY_WIN); sleep(1)
    type("r", KEY_WIN); sleep(1)
    type(appName); sleep(1)
    type(Key.ENTER)

def AdminLogin(username, password):
    click(MainPage.enterButton)
    wait(LoginPage.username)
    click(LoginPage.username)
    type(username)
    type(Key.TAB)
    type(password)
    click(LoginPage.submitButton)

def NavigateToMovedLectures():
    wait(MainPage.adminMenu)
    click(MainPage.adminMenu)
    wait(MainPage.adminMovedLectures)
    click(MainPage.adminMovedLectures)

def ClearGrid():
    wait(MovedLectures.removeItem)

    while exists(MovedLectures.removeItem):
        click(MovedLectures.removeItem)
        wait(MovedLectures.deletePopUp)
        click(MovedLectures.deletePopUp)

def FillInLectureFullDetails():
    wait(MovedLectures.popUpTitle)
    click(MovedLectures.courseDropDown)
    click(MovedLectures.courseDropDownOption)
    click(MovedLectures.startDate)
    type("a",KeyModifier.CTRL)
    type("01/01/2016 01:00:00")
    type(Key.TAB)
    type("01/01/2016 02:00:00")
    type(Key.TAB)
    type("Light")
    click(MovedLectures.updateButton)

def FillInLectureFullInvalidDetails():
    wait(MovedLectures.popUpTitle)
    click(MovedLectures.courseDropDown)
    click(MovedLectures.courseDropDownOption)
    click(MovedLectures.startDate)
    type("a",KeyModifier.CTRL)
    type("01/01/216 01:00:00")
    type(Key.TAB)
    type("01/01/2016 02:00:00")
    type(Key.TAB)
    type("Light")
    click(MovedLectures.updateButton)