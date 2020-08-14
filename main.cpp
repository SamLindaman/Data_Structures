//
//  main.cpp
//  HashTable
//
//  Created by Sam lindaman on 8/14/20.
//  Copyright © 2020 Sam lindaman. All rights reserved.
//

#include <iostream>
#include <list>
#include <string.h>

using namespace std;

class HashTable{
    list<string> *table;
    int max;
    
public:
    HashTable(int n){
        max = n;
        table = new list<string>[max];
    }
    
    int getHashKey(string key){
        int h = 0;
        for(int i = 0; i <key.length();i++){
            h += key[i];
        }
        return h % max;
    }
    
    void insert(string key){
        table[getHashKey(key)].push_back(key);
    }
    
    void remove(string key){
        int h = getHashKey(key);
        
        list<string>::iterator i;
        for (i=table[h].begin(); i!=table[h].end(); i++) {
            if(key.compare(i->c_str())){
                table[h].erase(i);
            }
        }
    }
    
    void print(){
        list<string>::iterator j;

        for(int i =0;i<max;i++){
            cout<< " Index: "<<i+1<<": ";
            for(j = table[i].begin();j!=table[i].end();j++){
                cout<<j->c_str()<<" -> ";
            }
            cout<<endl;
        }
        cout<<endl;
    }
    
};


int main(int argc, const char * argv[]) {
    
    //initialize hash table and fill it with elements
    HashTable hash(10);
    
    string arr[] = {"Sam", "Max", "Ada", "Jill", "Jan"};
    for(int i =0; i < (sizeof(arr)/sizeof(string)); i++){
        hash.insert(arr[i]);
    }
    
    hash.print();
    
    hash.insert("Madi");
    
    hash.remove("Max");
    
    hash.print();
    
    return 0;
}
