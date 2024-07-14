#include <iostream>
#include <limits.h>
using namespace std;

void addElement(int arr[], int &size, int element, int capacity)
{
  if (size < capacity)
  {
    arr[size] = element;
    size++;
  }
  else
  {
    cout << "Array is full, cannot add element!" << endl;
  }
}

void insertElement(int arr[], int &size, int element, int position, int capacity)
{
  if (position >= 0 && position <= size && size < capacity)
  {
    for (int i = size; i > position; i--)
    {
      arr[i] = arr[i - 1];
    }
    arr[position] = element;
    size++;
  }
  else
  {
    cout << "Invalid position or array is full!" << endl;
  }
}

int findMin(int arr[], int size)
{
  if (size == 0)
  {
    return INT_MAX;
  }

  int minElement = arr[0];

  for (int i = 1; i < size; i++)
  {
    if (arr[i] < minElement)
    {
      minElement = arr[i];
    }
  }

  return minElement;
}

int findMax(int arr[], int size)
{
  if (size == 0)
  {
    return INT_MIN;
  }

  int maxElement = arr[0];

  for (int i = 1; i < size; i++)
  {
    if (arr[i] > maxElement)
    {
      maxElement = arr[i];
    }
  }

  return maxElement;
}

int main()
{
  const int capacity = 10;
  int arr[capacity] = {1, 2, 3, 4, 5};
  int size = 5;

  addElement(arr, size, 6, capacity);
  for (int i = 0; i < size; i++)
  {
    cout << arr[i] << " ";
  }
  cout << endl;

  insertElement(arr, size, 10, 2, capacity);
  for (int i = 0; i < size; i++)
  {
    cout << arr[i] << " ";
  }
  cout << endl;

  cout << "Minimum element in the array: " << findMin(arr, size) << endl;
  cout << "Maximum element in the array: " << findMax(arr, size) << endl;

  return 0;
}
