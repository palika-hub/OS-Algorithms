#include<bits/stdc++.h>
using namespace std;

class Process{
    public:
        int pno;
        float arrivalTime;
        int priority;
        float burstTime;

    Process(int a, int b, float c, float d){
        this->pno = a;
        this->priority = b;
        this->arrivalTime = c;
        this->burstTime = d;
    }
};

class compares{
    public: 
    bool operator()(Process* a, Process* b){
        return a->priority < b->priority;
    }
};

void priorityScheduling(vector<Process*> process, int n){
    priority_queue<Process*,vector<Process*>,compares> pq;
    float currentTime = 0;
    int idx = 0;
    float waitTime = 0;
    while(!pq.empty() || idx < n ){
        while(idx < n && process[idx]->arrivalTime <= currentTime){
            pq.push(process[idx]);
            idx++;
        }
        if(!pq.empty()){
            Process* node = pq.top();
            pq.pop();
            cout<<"Process number: "<<node->pno<<" - "<<" "<<"Priority: "<<node->priority<<" - "<<"Arrival Time: "<<node->arrivalTime<<" - "<<"Burst Time: "<<node->burstTime<<" - "<< "Completion Time: ";
            currentTime+=node->burstTime;
            cout<<currentTime<<" - "<<"Turn Around Time: "<<currentTime - node->arrivalTime <<" - "<<"Wait Time: "<< currentTime - node->arrivalTime - node->burstTime<<endl;
            waitTime +=currentTime - node->arrivalTime - node->burstTime;

        }
        

    }
    cout<<"Average Time: "<<waitTime/(float)n<<endl;
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
    priorityScheduling(process,n);
    
}

