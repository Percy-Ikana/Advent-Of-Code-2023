#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <time.h>

using namespace std;

int wordToString(string word) {
    if (word.compare("one") == 0)
        return 1;
    if (word.compare("two") == 0)
        return 2;
    if (word.compare("three") == 0)
        return 3;
    if (word.compare("four") == 0)
        return 4;
    if (word.compare("five") == 0)
        return 5;
    if (word.compare("six") == 0)
        return 6;
    if (word.compare("seven") == 0)
        return 7;
    if (word.compare("eight") == 0)
        return 8;
    if (word.compare("nine") == 0)
        return 9;
    return -1;
}

int main()
{
    // Create and open a text file
    clock_t tStart = clock();
    vector<string> fileContents;
    string text;
    int sum = 0;

    ifstream MyFile("input");
    while (getline(MyFile, text)) {
        fileContents.insert(end(fileContents), text);
    }
    MyFile.close(); 
    //part 1
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Use a while loop together with the getline() function to read the file line by line
    for(string &text : fileContents) {
        // Output the text from the file
        int tempsum = 0;
        for (int i = 0; i<text.length(); i++){
            if (isdigit(text[i])) {
                tempsum += ((int)text[i]-48)*10;
                break;
            }
        }
        for (int i = text.length(); i>=0; i--){
            if (isdigit(text[i])) {
                tempsum += ((int)text[i]-48);
                break;
            }
        
        }
        sum+=tempsum;
    }
    cout << sum << endl;
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    //part2
    //step through 
    sum = 0;
    vector<string> nums = {"one","two","three","four","five","six","seven","eight","nine"};
    for(string &text : fileContents) {
        int earliestDigit;
        int earliestDigitIndex = 1000;
        int lastDigit;
        int lastDigitIndex = -1;

        //This collects both the earliest and last numerical digits found witin a string
        for (int i = 0; i<text.length(); i++){
            if (isdigit(text[i])) {
                earliestDigit = (int)text[i]-48;
                earliestDigitIndex = i;
                break;
            }
        }
        for (int i = text.length(); i>=0; i--){
            if (isdigit(text[i])) {
                lastDigit = (int)text[i]-48;
                lastDigitIndex = i;
                break;
            }
        }
        //ok, now to identify the spelled out digits, if any. I hate part 2 lol.
        
        string earliestString;
        int earliestStringIndex = 1000;
        string lastString;
        int lastStringIndex = -1;
        for (string &numText : nums) {
            int pos = text.find(numText);
            int lastPos = text.rfind(numText);
            if (pos != string::npos && pos < earliestStringIndex) {
                earliestStringIndex = pos;
                earliestString = numText;
            }
            if (lastPos != string::npos && lastPos > lastStringIndex) {
                lastStringIndex = lastPos;
                lastString = numText;
            }
        }
        //Now to compare these all to pick a final one from each
        int firstDig = earliestDigitIndex < earliestStringIndex ? earliestDigit : wordToString(earliestString);
        int lastDig = lastDigitIndex > lastStringIndex ? earliestDigit : wordToString(lastString);
        sum += firstDig*10+lastDig;
    }
    cout << sum << endl;
    printf("Time taken: %.5fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
}