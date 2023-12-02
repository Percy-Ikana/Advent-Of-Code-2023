#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <time.h>

using namespace std;

string part1(vector<string> data) {
    
    return "";
}

string part2(vector<string> data) {
    
    
    return "";
}

int main()
{
    // Create and open a text file
    vector<string> fileContents;
    string text;
    //read in the file. This is before timing, so we arent dealing with disk latency between machines in the timing.
    ifstream MyFile("input");
    while (getline(MyFile, text)) {
        fileContents.insert(end(fileContents), text);
    }
    MyFile.close(); 

    clock_t startTime = clock();
    cout << part2(fileContents) << endl << part2(fileContents) << endl;
    printf("Time taken: %.5fs\n", (double)(clock() - startTime)/CLOCKS_PER_SEC);
}