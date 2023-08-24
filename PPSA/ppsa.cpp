#include<bits/stdc++.h>
using namespace std;

class Process{
    public:
        int pno;
        int priority;
        float arrivalTime;
        float burstTime;
        float preTime;
    Process(int a, int b, float c, float d, float e = 0){
        this->pno = a;
        this->priority  =b;
        this->arrivalTime = c;
        this->burstTime = d;
        this->preTime = d;
    }
};

class compares{
    public:
        bool operator()(Process* a, Process* b){
            return a->priority < b->priority;
        }
};

void premptivePSA(vector<Process*> &process, int n){
    int idx = 0;
    priority_queue<Process*,vector<Process*>,compares> pq;
    float currentTime=0;
    float waitTime=0;
    while(!pq.empty() || idx < n){
        while(idx < n && process[idx]->arrivalTime <= currentTime){
            pq.push(process[idx]);
            idx++;
        }
        if(!pq.empty()){
            Process* p = pq.top();
            pq.pop();
            currentTime+=1;
            p->preTime-=1;
            if(p->preTime != 0){
                pq.push(p);
            }
            else{
                cout<<"Process number: "<<p->pno<<" - "<<" "<<"Priority: "<<p->priority<<" - "<<"Arrival Time: "<<p->arrivalTime<<" - "<<"Burst Time: "<<p->burstTime<<" - "<< "Completion Time: "<<
                currentTime<<" - "<<"Turn Around Time: "<< currentTime - p->arrivalTime << " - "<<"Wait Time: "<<currentTime - p->arrivalTime -p->burstTime<<endl;
                waitTime += currentTime - p->arrivalTime -p->burstTime;
            }

        }
    }
    cout<<"Average Waiting Time: "<<waitTime/(float)n<<endl;
}

int main(){
    int n;
    cout<<"Enter the number of processes: "<<endl;
    cin>>n;
    vector<Process*> process;
    for(int i = 0;i<n;i++){
        int pno;
        int pr;
        float at;
        float bt;
        cout<<"Enter process number: "<<endl;
        cin>>pno;
        cout<<"Enter the priority: "<<endl;
        cin>>pr;
        cout<<"Enter arrival time: "<<endl;
        cin>>at;
        cout<<"Enter burst time: "<<endl;
        cin>>bt;
        Process* p = new Process(pno,pr,at,bt);
        process.push_back(p);
    }
    premptivePSA(process,n);
    
}