#include<bits/stdc++.h>
using namespace std;


class Process{
    public:
        int pno;
        float arrivalTime;
        float burstTime;
    Process(int a, float b, float c){
        pno = a;
        arrivalTime = b;
        burstTime = c;
    }
};

class compares{
    public: 
        bool operator()(Process* a, Process* b){
            return a->burstTime > b->burstTime;
        }
};

void sjfAlgorithm(vector<Process*> process, int n){
    priority_queue<Process*,vector<Process*>,compares> pq;
    float currentTime= 0 ;
    long long int idx=0;
    float waitTime=0;
    while(!pq.empty() || idx < n){
        while(idx<n &&  process[idx]->arrivalTime <= currentTime){
            pq.push(process[idx]);
            idx++;
        }

        if(!pq.empty()){
            Process* node = pq.top();
            pq.pop();
            cout<<"Process Number : "<<node->pno<<" - "<<"Arrival Time : "<<node->arrivalTime<<" - "<<"Burst Time: "<<node->burstTime<<" - ";
            currentTime+=node->burstTime;
            cout<<"Completion Time: "<<currentTime<<" - "<<"Turn Around Time: "<<currentTime-node->arrivalTime<<" - "<<"Wait Time: "<<currentTime-node->arrivalTime-node->burstTime<<endl;
            waitTime += (currentTime - node->arrivalTime - node->burstTime);
        }
        else{
            currentTime+=1;
        }
    }
    cout<<"Average Wait Time: "<<waitTime/(float)n<<endl;
}

int main(){
    int n;
    cout<<"Enter the number of processes: "<<endl;
    cin>>n;
    vector<Process*> process;
    for(int i = 0;i<n;i++){
        int pno;
        float at;
        float bt;
        cout<<"Enter process number: "<<endl;
        cin>>pno;
        cout<<"Enter arrival time: "<<endl;
        cin>>at;
        cout<<"Enter burst time: "<<endl;
        cin>>bt;
        Process* p = new Process(pno,at,bt);
        process.push_back(p);
    }
    sjfAlgorithm(process,n);
}


