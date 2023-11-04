#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is palindrome
 * or not
 * @head: singly linked list pointer.
 *
 * Return: 1 if palindrome, 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *control = *head, *tracker_1 = *head, *hold = *head, *end;

	if (!*head || !(*head)->next)
	{
		return (1);
	}
	while (true)
	{
		tracker_1 = tracker_1->next->next;
		if (!tracker_1)
		{
			end = control->next;
			break;
		}
		if (!tracker_1->next)
		{
			end = control->next->next;
			break;
		}
		control = control->next;
	}

	reverse_listint(&end);

	while (end && hold)
	{
		if (hold->n == end->n)
		{
			end = end->next;
			hold = hold->next;
		}
		else
		{
			return (0);
		}
	}
	return (0);
}

/**
 * reverse_listint - reverses a singly linked list
 * @head: head (first) node of the list.
 *
 * Return: head of the new list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *temp, *hold;

	temp = NULL;
	while (*head)
	{
		hold = (*head)->next;
		(*head)->next = temp;
		temp = *head;
		*head = hold;
	}
	*head = temp;
	return (*head);
}
