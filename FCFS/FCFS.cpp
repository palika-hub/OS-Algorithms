#include<bits/stdc++.h>
using namespace std;


class Process{
    public:
        int pno;
        int arrivalTime;
        int burstTime;
    Process(int a, int b, int c){
        pno = a;
        arrivalTime = b;
        burstTime = c;
    }
};

class compares{
    public: 
        bool operator()(Process* a, Process* b){
            return a->arrivalTime > b->arrivalTime;
        }
};

void printFCFS(vector<Process*> &process, int n){
    priority_queue<Process*, vector<Process*> , compares> pq;
    for(auto it: process){
        pq.push(it);
    }
    int cTime=0;
    float wTime=0;
    while(!pq.empty()){
        Process* p = pq.top();
        pq.pop();
        cTime+=p->burstTime;
        cout<<"Process Name: "<<p->pno<<" - "<<"Arrival Time: "<<p->arrivalTime<<" - "<<"Burst Time: "<<p->burstTime<<" - "<<"Completion Time: "<<cTime<<" - "<<"TurnAroundTime: "<<cTime - p->arrivalTime<<" - "<<
        "Wait Time: "<<cTime - p->arrivalTime - p->burstTime<<endl;
        wTime+=cTime - p->arrivalTime - p->burstTime;
    }
    
    cout<<"Average Wait Time: "<<wTime/(float)n<<endl;
}
int main(){
    int n;
    cout<<"Enter the number of Processes:"<<endl;
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
    printFCFS(process,n);
}