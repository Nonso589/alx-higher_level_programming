#include "lists.h"
/**
 * check_cycle - checks if a linked list is circular or not
 *
 * @list: linked list to check
 *
 * Return: 1 (linked list is circular) 0 (no loop detected)
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = NULL, *fast = NULL;

	slow = fast = list;
	while (list && slow && fast && slow->next && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (!fast || !slow)
			return (0);
		if (fast->next == slow)
			return (1); /* loop found */
	}
	/* no loop detected */
	return (0);
}
