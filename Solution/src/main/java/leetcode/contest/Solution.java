package leetcode.contest;

import java.util.ArrayList;

public class Solution {
    // Harshad Number
//    public static int sumOfTheDigitsOfHarshadNumber(int x) {
//        int temp = x;
//        ArrayList<Integer> X = new ArrayList<Integer>();
//        while(temp>=1){
//            X.add(temp%10);
//            temp = temp/10;
//        }
//        int SUM = 0;
//        int size = X.size();
//        for (int i = 0; i<size; i++){
//            SUM = SUM + X.get(i);
//        }
//        if(x%SUM ==0) return SUM;
//        return -1;
//    }
//    public static int maxBottlesDrunk(int numBottles, int numExchange) {
//        int totalBottle = numBottles;
//        while(numBottles!=0 && numExchange<=numBottles){
//            numBottles = numBottles - numExchange +1;
//            totalBottle++;
//            numExchange++;
//        }
//
//        return totalBottle;
//    }
//    public static long countAlternatingSubarrays(int[] nums) {
//        int X = nums.length;
//        int total = 0;
//        for (int i = 0; i<X; i++ ){
//            for (int j = i; j<X; j++){
//                if (i == j) total++;
//                else {
//                    int prev = nums[i];
//                    int flag = 0;
//                    for (int k = i+1; k<=j; k++){
//                        if (nums[k] == prev) {flag = 1;break;}
//                        else {prev = nums[k];}
//                    }
//                    if (flag !=1) total++;
//                }
//
//            }
//        }
//        return total;
//    }
    public static int minimumDistance(int[][] points) {
        
        return 0;
    }
    public static void main(String[] args){
//        int[] num = {1,0,1,0};
//        System.out.println(countAlternatingSubarrays(num));
        int[][] points = {{3,10},{5,15},{10,2},{4,4}};
        System.out.println(minimumDistance(points));
    }
}
