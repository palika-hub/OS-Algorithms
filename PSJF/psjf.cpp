#include<bits/stdc++.h>
using namespace std;

class Process{
    public:
        int pno;
        float arrivalTime;
        float burstTime;
        float preTime;
    Process(int a, float c, float d, float e = 0){
        this->pno = a;
        this->arrivalTime = c;
        this->burstTime = d;
        this->preTime = d;
    }
};

class compares{
    public:
        bool operator()(Process* a, Process* b){
            return a->burstTime > b->burstTime;
        }
};

void preemptiveSJF(vector<Process*> &process, int n){
    priority_queue<Process*,vector<Process*>,compares> pq;
    float waitTime = 0;
    float currentTime = 0;
    int idx = 0;
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
            if(p->preTime == 0){
                cout<<"Process Name: "<<p->pno<<" - "<<"Arrival Time: "<<p->arrivalTime<<" - "<<"Burst Time: "<<p->burstTime<<" - "
                <<"Completion Time: "<<currentTime<<" - "<<"Turn Around Time: "<<currentTime - p->arrivalTime<<" - "<<"Wait Time: "<<currentTime - p->arrivalTime - p->burstTime
                <<" - "<<endl;
                waitTime+=currentTime - p->arrivalTime - p->burstTime;
            }
            else{
                pq.push(p);
            }
        }
    }
    cout<<"Average Wait time: "<<waitTime/(float)n<<endl;

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
    // premptivePSA(process,n);
    preemptiveSJF(process,n);
    
}