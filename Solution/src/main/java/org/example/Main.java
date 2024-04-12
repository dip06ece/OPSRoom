package org.example;

import java.util.ArrayList;
import java.util.stream.Collectors;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {

    public static void main(String[] args) {
        ArrayList<Integer> myList = new ArrayList<>();
        for (int i = 'a'; i<='z';i++){
            myList.add(0);
        }
        String x = "This is a test";
        for (int i=0;i<x.length(); i++){
            char y = x.charAt(i);
            if(y!=' '){
                y = Character.toLowerCase(y);
                myList.set(y-'a', myList.get(y-'a')+1);
            }
        }
        System.out.println(myList.toString());
        System.out.println(myList.stream().collect(Collectors.summingInt(Integer::intValue)));
        }
    }