#include "lists.h"
/**
 * check_cycle - checks wether or not a singly linked list has a cycle
 * @list: the singly linked list
 * Return: (1) if there is a cycle or (0) otherwize
*/
int check_cycle(listint_t *list)
{
listint_t *head = list, *temp = list;
while (head != NULL && head->next != NULL)
{
temp = temp->next;
head = head->next->next;
if (temp == head)
{
return (1);
}

}
return (0);
}
