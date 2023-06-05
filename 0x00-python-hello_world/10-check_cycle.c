#include "lists.h"

/**
 * check_cycle - checles if the singly-linked list has a cycle in it
 *
 * It takes two pointers one moving one node at a time another two nodes
 * at a time if the pointers meet there is a cycle
 * @list: pointer to the first node of the list
 * Return: 0 if thereis no cycle, 1 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp_1 = list;
	listint_t *tmp_2 = list;

	if (list == NULL)
	{
		return (0);
	}

	while (tmp_1 != NULL && tmp_1->next != NULL)
	{
		tmp_2 = tmp_2->next;
		tmp_1 = tmp_1->next->next;

		if (tmp_2 == tmp_1)
		{
			return (1);
		}

	}

	return (0);
}
