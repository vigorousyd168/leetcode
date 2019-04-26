/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode curr = head;
        if (curr == null) return null;
        ListNode res = head.next;
        if (res == null) return head;
        ListNode prev = null;
        while (curr!= null && curr.next != null) {
            ListNode next = curr.next;
            curr.next = next.next;
            next.next = curr;
            if (prev != null) prev.next = next;
            prev = curr;
            curr = curr.next;
        }
        return res;
    }
}