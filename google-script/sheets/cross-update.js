/* 

- Developed May 22, 2020 - Paras Lehana (contact for updation and queries).
- Requirement by Samarendra Pratap. 
- Function to update values from one sheet to another for a given row to save horizontal scroll. 

*/



function crossUpdate() {

    // Names of source and destination sheets
    const sourceSheet = 'Sheet9';
    const destinationSheet = 'Post Corona (Pradeep)';
    
    // Cell in source sheet that has the destination row number indexed from 0
    const destinationRowCell = 'B2';
    
    // Map of (Source Cell, Destination Column) pairs. Source Cell value will be pasted to Destination Column and the given row
    var cellMap = {'F5': 'B', 'F6': 'W'};
    
    var spreadsheet = SpreadsheetApp.getActive();
    
    // Fetch the concerned destination row (indexed from 0)
    var destinationRow = 1 + spreadsheet.getRange(sourceSheet + '!' + destinationRowCell).getValue();
    
    // For each entry in cellMap, paste value to concerned cell
    for (sourceCell in cellMap) {
      
      var destinationCell = cellMap[sourceCell] + destinationRow;
    
      spreadsheet.setActiveSheet(spreadsheet.getSheetByName(destinationSheet), true);
      spreadsheet.getRange(destinationCell).activate();
      spreadsheet.getRange(sourceSheet + '!' + sourceCell).copyTo(spreadsheet.getActiveRange(), SpreadsheetApp.CopyPasteType.PASTE_NORMAL, false);
      
    }
    
    
  };
  
  