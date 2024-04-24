import xlwings as xw
workbook_path = "C:\\Users\\X250380\\OneDrive - MerckGroup\\Desktop\\SoPo Macro\\Macro_file_1.xlsm"
macro_name ="MainZCBB.MainZCBB"
macro_name2 ="mainZCOR.ZCOR"
try

        # Start an Excel application
        app = xw.App(visible=False)  # visible=False hides the Excel application window

        # Open the workbook
        workbook = app.books.open(workbook_path)

        # Run the macro
        workbook.macro(macro_name)()
        workbook.macro(macro_name2)()


        # Save and close the workbook
        workbook.save()
        workbook.close()
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Quit the Excel application
    app.quit()
