#include "lists.h"

/**
 * check_cycle - checks if there's a cycle in a singly
 * linked list.
 *
 * @list: list to check
 *
 * Return:	0 if no cycle
 *		1 if there's one
 */
int check_cycle(listint_t *list)
{
	listint_t *head_1, *head_2;

	if (!list)
	{
		return (0);
	}
	head_1 = list;
	head_2 = list->next;
	while (head_1 && head_2 && head_2->next)
	{
		if (head_1 == head_2)
		{
			return (1);
		}
		head_1 = head_1->next;
		head_2 = head_2->next->next;
	}
	return (0);
}
