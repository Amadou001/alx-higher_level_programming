#include "lists.h"
/**
 * is_palindrome - checks whether a singly linked list is a palindrome
 * or not
 * @head: a pointer to the list
 * Return: 1 if it is a palindrome or 0 otherwise
*/
int is_palindrome(listint_t **head)
{
listint_t *temp;
int *list, *reverse_list;
int i = 0;
list = (int *)malloc(sizeof(int));
if (list == NULL)
{
return (0);
}
temp = *head;
while (temp != NULL)
{
list[i] = temp->n;
list = realloc(list, sizeof(int) * (i + 2));
if (list == NULL)
{
free(list);
return (0);
}
temp = temp->next;
i++;
}
reverse_list = (int *)malloc(sizeof(int) * i);
if (reverse_list == NULL)
{
free(list);
return (0);
}
return (list_rev_compare(&list, &reverse_list, i));
}

/**
 * list_rev_compare - reverses and compares lists
 * @list_1: pointer to list 1
 * @list_2: pointer to list 2
 * @i: number of elements
 * Return: 1 if both lists are equal or 0 otherwise
*/
int list_rev_compare(int **list_1, int **list_2, int i)
{
int k, j;
for (j = 0; j < i; j++)
{
(*list_2)[j] = (*list_1)[i - j - 1];
}
for (k = 0; k < i; k++)
{
if ((*list_2)[k] != (*list_1)[k])
{
free(*list_1);
free(*list_2);
return (0);
}
}
free(*list_1);
free(*list_2);
return (1);
}
