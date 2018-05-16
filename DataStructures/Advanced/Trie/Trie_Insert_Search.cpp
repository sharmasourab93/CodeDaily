//Trie Handson
#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<stdio.h>
#include<stdbool.h>
using namespace std;
#define ARRAY_SIZE(a) sizeof(a)/sizeof(a[0])
#define ALPHA_SIZE (26)
#define CHAR_TO_INDEX(c) ((int)c - (int)'a')
struct TrieNode{
	TrieNode *children[ALPHA_SIZE];
	bool isLeaf;
};
TrieNode *getNode(void){
	TrieNode *pNode=NULL;
	pNode=new TrieNode();
	if(pNode){
		int i;
		pNode->isLeaf=false;
		for(i=0;i<ALPHA_SIZE;i++){
			pNode->children[i]=NULL;
		}
	}
	return pNode;
}
void insert(TrieNode *root,const char *key){
	int level;
	int length=strlen(key);
	int index;
	TrieNode *pCrawl=root;
	for(level=0;level<length;level++){
		index=CHAR_TO_INDEX(key[level]);
		if(!pCrawl->children[index]){
			pCrawl->children[index]=getNode();
		}
		pCrawl=pCrawl->children[index];
	}
	pCrawl->isLeaf=true;
}
bool search(TrieNode *root, const char *key){
	int level;
	int length=strlen(key);
	int index;
	TrieNode *pCrawl=root;
	for(level=0;level<length;level++){
		index=CHAR_TO_INDEX(key[level]);
		if(!pCrawl->children[index]) return false;
		pCrawl=pCrawl->children[index];
	}
	return (pCrawl!=NULL&& pCrawl->isLeaf);
}
int main(){
	char keys[][]={"the","a","there","answer","any","by","bye","their"};
	char output[][32]={"Not present in trie","Present in trie"};
	TrieNode *root=getNode();
	int i;
	for(i=0;i<ARRAY_SIZE(keys);i++) 
		insert(root,keys[i]);
	printf("%s --- %s","the",output[search(root,"the")]);
	printf("%s --- %s","these",output[search(root,"these")]);
	printf("%s --- %s","their",output[search(root,"their")]);
	printf("%s --- %s","thaw",output[search(root,"thaw")]);
	
}
