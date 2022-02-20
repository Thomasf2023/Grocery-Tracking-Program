/*The purpose of this program is to combine C++ and Python to create a program that the user can use to see how often an item is 
being sold in a given day, search for an item and see the number of purchases that were made for that item, and see a histogram of sales
for each item.
Author: Thomas Fiske
Date: 2/15/2022 
*/

#include <Python.h>
#include <iostream>
#include <Windows.h>
#include <cmath>
#include <string>
#include <chrono>
#include <thread>
#include <stdlib.h>
#include <fstream>
#include <list>

using namespace std;

/*
Description:
	To call this function, simply pass the function name in Python that you wish to call.
Example:
	callProcedure("printsomething");
Output:
	Python will print on the screen: Hello from python!
Return:
	None
*/
void CallProcedure(string pName)
{
	char* procname = new char[pName.length() + 1];
	std::strcpy(procname, pName.c_str());

	Py_Initialize();
	PyObject* my_module = PyImport_ImportModule("PythonCode");
	PyErr_Print();
	PyObject* my_function = PyObject_GetAttrString(my_module, procname);
	PyObject* my_result = PyObject_CallObject(my_function, NULL);
	Py_Finalize();

	delete[] procname;
}

/*
Description:
	To call this function, pass the name of the Python functino you wish to call and the string parameter you want to send
Example:
	int x = callIntFunc("PrintMe","Test");
Output:
	Python will print on the screen:
		You sent me: Test
Return:
	100 is returned to the C++
*/
int callIntFunc(string proc, string param)
{
	char* procname = new char[proc.length() + 1];
	std::strcpy(procname, proc.c_str());

	char* paramval = new char[param.length() + 1];
	std::strcpy(paramval, param.c_str());


	PyObject* pName, * pModule, * pDict, * pFunc, * pValue = nullptr, * presult = nullptr;
	// Initialize the Python Interpreter
	Py_Initialize();
	// Build the name object
	pName = PyUnicode_FromString((char*)"PythonCode");
	// Load the module object
	pModule = PyImport_Import(pName);
	// pDict is a borrowed reference 
	pDict = PyModule_GetDict(pModule);
	// pFunc is also a borrowed reference 
	pFunc = PyDict_GetItemString(pDict, procname);
	if (PyCallable_Check(pFunc))
	{
		pValue = Py_BuildValue("(z)", paramval);
		PyErr_Print();
		presult = PyObject_CallObject(pFunc, pValue);
		PyErr_Print();
	}
	else
	{
		PyErr_Print();
	}
	//printf("Result is %d\n", _PyLong_AsInt(presult));
	Py_DECREF(pValue);
	// Clean up
	Py_DECREF(pModule);
	Py_DECREF(pName);
	// Finish the Python Interpreter
	Py_Finalize();

	// clean 
	delete[] procname;
	delete[] paramval;


	return _PyLong_AsInt(presult);
}

/*
Description:
	To call this function, pass the name of the Python functino you wish to call and the string parameter you want to send
Example:
	int x = callIntFunc("doublevalue",5);
Return:
	25 is returned to the C++
*/
int callIntFunc(string proc, int param)
{
	char* procname = new char[proc.length() + 1];
	std::strcpy(procname, proc.c_str());

	PyObject* pName, * pModule, * pDict, * pFunc, * pValue = nullptr, * presult = nullptr;
	// Initialize the Python Interpreter
	Py_Initialize();
	// Build the name object
	pName = PyUnicode_FromString((char*)"PythonCode");
	// Load the module object
	pModule = PyImport_Import(pName);
	// pDict is a borrowed reference 
	pDict = PyModule_GetDict(pModule);
	// pFunc is also a borrowed reference 
	pFunc = PyDict_GetItemString(pDict, procname);
	if (PyCallable_Check(pFunc))
	{
		pValue = Py_BuildValue("(i)", param);
		PyErr_Print();
		presult = PyObject_CallObject(pFunc, pValue);
		PyErr_Print();
	}
	else
	{
		PyErr_Print();
	}
	//printf("Result is %d\n", _PyLong_AsInt(presult));
	Py_DECREF(pValue);
	// Clean up
	Py_DECREF(pModule);
	Py_DECREF(pName);
	// Finish the Python Interpreter
	Py_Finalize();

	// clean 
	delete[] procname;

	return _PyLong_AsInt(presult);
}

void printUserItem() { // This function uses python to get the quantity of an item and return that quantity to the user.
	string userItem;
	int userItemQuantity;

	cout << "Please enter your item name with the first letter capitalized Ex. Cucumbers" << endl;
	cin >> userItem;
	userItemQuantity = callIntFunc("givenItemQuantity", userItem);
	cout << "You chose: " << userItem << endl;
	cout << endl;
	cout << "Quantity of " << userItem << ": " << userItemQuantity << endl;

}


int main() {
	int userMenuChoice;
	int nextChoice;
	boolean menuLoop = true;
   
	


	 while (menuLoop == true) { // This loop will run until the user exit's the program.
		CallProcedure("displayMenu");
		cin >> userMenuChoice;
		cout << "You selected: " << userMenuChoice << endl;
		cout << endl;

		if (userMenuChoice == 1) { // This branch will take the user to the individual item quantity selection.
			cout << endl;
			CallProcedure("individualItemQuantity");
			cout << endl;
			cout << "Do you wish to return to the main menu?" << endl; // This message will allow the user to exit or return to the menu
			cout << "(1): Yes" << endl;
			cout << "(2): No/Exit" << endl;
			cout << "Please enter 1 or 2" << endl;
			cin >> nextChoice;
			if (nextChoice == 1) {
				continue;
				Sleep(1000);
				system("CLS");

			}
			else if (nextChoice == 2) {
				cout << "Now Exiting: Thank you for using our program" << endl;
				break;
			}
			else {
				cout << "Error: Invalid Entry. Returning to the main menu";

			}
		}
		else if (userMenuChoice == 2) { // This branch takes the user to option 2: Quantity of item that is searched.
			printUserItem();
			cout << endl;
			cout << "Do you wish to return to the main menu?" << endl;
			cout << "(1): Yes" << endl;
			cout << "(2): No/Exit" << endl;
			cout << "Please enter 1 or 2" << endl;
			cin >> nextChoice;
			if (nextChoice == 1) {
				continue;
				Sleep(1000);
				system("CLS");

			}
			else if (nextChoice == 2) {
				cout << "Now Exiting: Thank you for using our program" << endl;
				break;
			}
			else {
				cout << "Error: Invalid Entry. Returning to the main menu";

			}
		

		}
		else if (userMenuChoice == 3) { // This branch will call a function to create the histogram.
			
			CallProcedure("histrogramCreator");
			
			cout << endl;
			cout << "Do you wish to return to the main menu?" << endl;
			cout << "(1): Yes" << endl;
			cout << "(2): No/Exit" << endl;
			cout << "Please enter 1 or 2" << endl;
			cin >> nextChoice;
			if (nextChoice == 1) {
				continue;
				Sleep(1000);
				system("CLS");

			}
			else if (nextChoice == 2) {
				cout << "Now Exiting: Thank you for using our program" << endl;
				break;
			}
			else {
				cout << "Error: Invalid Entry. Returning to the main menu";

			}

		}
		else if (userMenuChoice == 4) { // Exit branch
			cout << "Now Exiting: Thank you for using our program" << endl;
			break;
		}
		else {
			cout << "Error: Invalid input, please try again";
			cin >> userMenuChoice;
			cout << "You selected: " << userMenuChoice << endl;
			cout << endl;
		}
	}
	
	return 0;
}
