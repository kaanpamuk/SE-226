#include <iostream>
using namespace std;


void printArray(int* arr, int size){
    int*p=&arr[0];
    for (int i=0;i<size;i++) {
        cout<<*p<<endl;
        p++;
    }
}

void swapValues(int* p1, int* p2){
    int temp = *p1;
    *p1 = *p2;
    *p2 =temp;
}

int findSum(int* arr, int size){
    int sum = 0;
    int* p = arr;
    for(int i = 0; i < size; i++){
        sum += *p;
        p++;
    }

    return sum;
}

void shiftRight(int* arr, int size){
    int last = arr[size-1];

    for(int i = size-1; i > 0; i--) {
        arr[i] = arr[i-1];
    }
    arr[0] = last;
}

int* createArray(int size){
    int* array = new int[size];

    cout << "Enter values: ";
    for(int i = 0; i < size; i++){
        cin >> array[i];
    }

    return array;
}

void deleteArray(int* arr){
    cout << "Deleting array..." << endl;
    delete[] arr;
    cout << "Memory released successfully." << endl;
}

int main() {
    

    int array []={1,2,3,4,5};

    cout<<"Print Array:"<<endl;
    printArray(array,5);

    int f1=5;
    int f2=8;

    swapValues(&f1, &f2);

    cout<<"Swap Values:"<<endl;
    cout<<f1<<endl;
    cout<<f2<<endl;

    cout<<"Find Sum:"<<endl;
    cout<<findSum(array,5)<<endl;

    shiftRight(array,5);

    cout<<"Shift Right:"<<endl;
    for(int i=0;i<5;i++) {
        cout << array[i] << " ";
    }
    cout<<endl;

    int size;
    cout << "Enter array size: ";
    cin >> size;

    int* arr = createArray(size);

    cout << "Array elements: ";
    for(int i = 0; i < size; i++){
        cout << arr[i] << " ";
    }
    cout<<endl;

    int sum = findSum(arr,size);
    cout << "Sum of elements: " << sum << endl;

    deleteArray(arr);

    return 0;
}