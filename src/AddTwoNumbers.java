
public class AddTwoNumbers {

	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		ListNode answers = new ListNode(0);
		ListNode answers_head = answers;
		int val;
		int carrySum;


		for(;l1 != null && l2 != null;){

			val = (answers.val + l1.val + l2.val) % 10;
			carrySum = (answers.val + l1.val + l2.val) / 10;
			answers.val = val;

			l1 = l1.next;
			l2 = l2.next;

			if(l1 == null && l2 == null && carrySum == 0){
				return answers_head;
			}
			else if (l1 == null && l2 == null && carrySum > 0){
				answers.next = new ListNode(carrySum);   
				return answers_head;
			}
			else if(l1 != null || l2 != null){
				answers.next = new ListNode(carrySum);   
				answers = answers.next; 
			}

		}

		if(l1 == null){

			for(;l2 != null;){

				val = (answers.val + l2.val) % 10;
				carrySum = (answers.val + l2.val) / 10;
				answers.val = val;
				l2 = l2.next;

				if(l2 == null && carrySum == 0){
					return answers_head;
				}
				else if(l2 != null || carrySum > 0){
					answers.next = new ListNode(carrySum);
					answers = answers.next;
				}
			}

		}

		if(l2 == null){

			for(;l1 != null;){

				val = (answers.val + l1.val) % 10;
				carrySum = (answers.val + l1.val) / 10;
				answers.val = val;
				l1 = l1.next;

				if(l1 == null && carrySum == 0){
					return answers_head;
				}
				else if(l1 != null || carrySum > 0){
					answers.next = new ListNode(carrySum);
					answers = answers.next;
				}
			}

		}

		return answers_head;
	}

	public class ListNode {
		int val;
		ListNode next;
		ListNode(int x) { val = x; }
	}

}

