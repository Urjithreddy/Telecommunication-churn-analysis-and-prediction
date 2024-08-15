#include <stdio.h>
#include <string.h>

#define MAX_STUDENTS 100

struct Student {
    int sno;
    char sname[50];
    int marks;
    char grade;
};

// Function to calculate grade based on marks
char calculate_grade(int marks) {
    if (marks >= 90) {
        return 'A';
    } else if (marks >= 80) {
        return 'B';
    } else if (marks >= 70) {
        return 'C';
    } else if (marks >= 60) {
        return 'D';
    } else {
        return 'F';
    }
}

// Function to sort students in descending order of marks (using bubble sort)
void sort_students(struct Student students[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (students[j].marks < students[j + 1].marks) {
                // Swap students[j] and students[j + 1]
                struct Student temp = students[j];
                students[j] = students[j + 1];
                students[j + 1] = temp;
            }
        }
    }
}

int main() {
    struct Student students[MAX_STUDENTS];
    int n;

    printf("Enter the number of students: ");
    scanf("%d", &n);

    // Get student details
    for (int i = 0; i < n; i++) {
        printf("\nEnter details for student %d:\n", i + 1);
        printf("Serial Number: ");
        scanf("%d", &students[i].sno);
        printf("Name: ");
        scanf("%s", students[i].sname);
        printf("Marks: ");
        scanf("%d", &students[i].marks);

        // Calculate and assign grade
        students[i].grade = calculate_grade(students[i].marks);
    }

    // Sort students based on marks
    sort_students(students, n);

    // Print the sorted list of students
    printf("\nSorted Student Records:\n");
    for (int i = 0; i < n; i++) {
        printf("Sno: %d, Name: %s, Marks: %d, Grade: %c\n",
               students[i].sno, students[i].sname, students[i].marks, students[i].grade);
    }

    return 0;
}
