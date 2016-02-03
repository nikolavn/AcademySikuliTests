########################################################
# UI map for XYZ
########################################################
from sikuli import *
########################################################
class LoginPage:

    username = "username.png"

    password = "password.png"

    submitButton = "submitButton.png"

class MainPage:

    enterButton = Pattern("enterButton.png").targetOffset(-43,-2)

    adminMenu = Pattern("adminMenu.png").similar(0.87)

    adminMovedLectures = "adminMovedLectures.png"
    
class MovedLectures:

    addNewItem = "addNewItem.png"

    removeItem = "removeItem.png"

    editItem = "editItem.png"

    refreshGrid = Pattern("refreshGrid.png").targetOffset(29,2)

    popUpTitle = "1453407407372.png"

    courseDropDown = Pattern("courseDropDown.png").similar(0.80).targetOffset(-84,-3)

    startDate = Pattern("startDate.png").targetOffset(53,-6)

    endDate = Pattern("endDate.png").targetOffset(-91,-2)

    trainingRoomDropDown = Pattern("trainingRoomDropDown.png").targetOffset(-71,1)

    updateButton = Pattern("updateButton.png").similar(0.80)

    cancelButton = "cancelButton.png"

    validForAllCOursesText = "validForAllCOursesText.png"

    allCoursesList = "allCoursesList.png"

    courseDropDownOption = "courseDropDownOption.png"


    courseFilterDropDownAllCourses = "courseFilterDropDown.png"

    deletePopUp = Pattern("deletePopUp.png").targetOffset(-32,6)

    validForAllTrainingRooms = "validForAllTrainingRooms.png"

    startDateValidationError = "startDateValidationError.png"

    courseValidationError = "1453411922065.png"
         

    validEntry = Pattern("validEntry.png").similar(0.32)

    emptyGrid = "emptyGrid.png"

    coursesFilterDropdown = Pattern("coursesFilterDropdown.png").targetOffset(215,0)

    coursesFilterDropdownAllSelected = Pattern("coursesFilterDropdownAllSelected.png").targetOffset(217,2)

    coursesFilterDropdownAllSelectedManualEntry = "coursesFilterDropdownAllSelectedManualEntry.png"


    consoleWindow = "consoleWindow.png"


    exportToPDF = "exportToPDF.png"

    exportPopUp = "exportPopUp.png"

    
    

    exportedValidEntry = "exportedValidEntry.png"
    