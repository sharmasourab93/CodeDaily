#include<iostream>
#include<stdio.h>
#include<cstring>
//using namespace std;
#define ALPHABET_SIZE (26)
#define ARRAY_SIZE(a) sizeof(a)/sizeof(a[0])
#define CHAR_TO_INDEX(c) ((int)c-(int)'a')
struct TrieNode{
	TrieNode *children[ALPHABET_SIZE];
	bool isLeaf;
};
TrieNode *getNode(void){
	TrieNode *pNode=NULL;
	pNode=new TrieNode();
	if(pNode){
		int i;
		pNode->isLeaf=false;
		for(i=0;i<ALPHABET_SIZE;i++){
			pNode->children[i]=NULL;
		}
	}
	return pNode;
}
void insert(TrieNode *root, const char *key){
	int level;
	int length=strlen(key);
	int index;
	TrieNode *pCrawl=root;
	for(level=0;level<length;level++){
		index=CHAR_TO_INDEX(key[level]);
		if(!pCrawl->children[index])
			pCrawl->children[index]=getNode();
		pCrawl=pCrawl->children[index];
	}
	pCrawl->isLeaf=true;
}
bool search(TrieNode *root,const char *key){
	int level;
	int length=strlen(key);
	int index;
	TrieNode *pCrawl=root;
	for(level=0;level<length;level++){
		index=CHAR_TO_INDEX(key[level]);
		if(!pCrawl->children[index]) return false;
		pCrawl->children[index];
	}
	return (pCrawl!=NULL && pCrawl->isLeaf);
}
int main(){
	char keys[][8]={"the","a","there","answer","any","by","bye","their"};
	char output[][32]={"Not present in trie","Present in trie"};
	TrieNode *root=getNode();
	int i;
	for(i=0;i<ARRAY_SIZE(keys);i++){
		insert(root, keys[i]);
	}
	printf("%s --- %s\n","the",output[search(root,"the")]);
}
