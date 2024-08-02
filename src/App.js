import logo from './logo.svg';
import './App.css';
import Nav from './components/nav.js'
import background from './finback.jpg'
import background1 from './fb2.jpg'
import Body from './components/Body.js'
import Taskbar from './components/Taskbar.js'
import Terminal from "./components/terminal.js"
import { useState, useEffect } from 'react';
import gear from "./gear.svg";
import backlock from "./fb1.jpg"
// import backlock from "./backlock.jpg"
import { Rnd } from 'react-rnd';
import Simulationwindow from './components/Simulationwindow.js';
import FCFS from './components/simulations/FCFS.js';

function App() {
  const [isDragging, setIsDragging] = useState(true);
  const [screenopen,setscreenopen] = useState(false);
  const [issim,setissim] = useState("");
  const [instpassed,setinstpassed] = useState("");
  const [name,setname] = useState('');
  const [windows,setwindows] = useState([{heading:"Window",state:false,zi:0},{heading:"Help",state:false,zi:0},{heading:"Simulations",state:false,zi:0},{heading:"Preferences",state:false,zi:0},{heading:"Music",state:false,zi:0},{heading:"Pictures",state:false,zi:0},{heading:"Videos",state:false,zi:0},{heading:"Documents",state:false,zi:0},{heading:"Page-Replacement",state:false,zi:0},{heading:"Applications",state:false,zi:0},{heading:"FCFS",state:false,zi:0},{heading:"SJF",state:false,zi:0},{heading:"RR",state:false,zi:0},{heading:"Priority Preemptive",state:false,zi:0},{heading:"Priority Non Preemptive",state:false,zi:0},{heading:"IRRVQ",state:false,zi:0},{heading:"CPU Scheduling",state:false,zi:0},{heading:"Dynamic Storage Allocation",state:false,zi:0},{heading:"First Fit",state:false,zi:0},{heading:"Next Fit",state:false,zi:0},{heading:"Best Fit",state:false,zi:0},{heading:"Worst Fit",state:false,zi:0},{heading:"Producer-Consumer.exe",state:false,zi:0},{heading:"Semaphores.exe",state:false,zi:0},{heading:"Dining-Philosophers.exe",state:false,zi:0},{heading:"FIFO",state:false,zi:0},{heading:"LRU",state:false,zi:0},{heading:"MRU",state:false,zi:0},{heading:"Optimal",state:false,zi:0}]);
  const handleDragStart = () => {
    setIsDragging(true);
  };
  const [terminalz,setterminalz] = useState(0);
  useEffect(() => {console.log("simulation systems engaged")},[issim]);
  useEffect(() => {console.log("simulation systems engaged on Instruction")},[instpassed]);
  useEffect(() => {console.log("dragging changed")},[isDragging]);

  const handleDragStop = () => {
    setIsDragging(false);
  };
  const [isLoading, setIsLoading] = useState(true);
  const [islocked,setlocked] = useState(true);
  const unlock = (e) =>{
    if (document.getElementById('pass').value === 'admin'){
    setlocked(false);
    }else{
      // alert('Wrong Password');
      document.getElementById('pass').placeholder="Wrong Password try again...";
      document.getElementById('pass').value="";
    }
  }
 
    setTimeout(() => {
        setIsLoading(false);
    }, 3000);
  return (
    <div style={{overflow:'hidden',height:'100vh',width:'100vw'}}>
    <div style={(isLoading)?{display:'flex',flexDirection:'column',justifyContent:'center',alignItems:'center',backgroundImage:`url(${background1})`,width:'100vw',height:'100vh',backgroundRepeat:'no-repeat',backgroundAttachment:'fixed',backgroundPosition:'center',backgroundSize:'cover'}:{display:'none'}}>
      <img src="https://p3d.in/static/uploads/94995/image-db241279986.png"/>
      <img src={gear}></img>

      
    </div>
    <div style={(islocked)?{display:'flex',flexDirection:'column',justifyContent:'center',alignItems:'center',backgroundImage:`url(${background})`,width:'100vw',height:'100vh',backgroundRepeat:'no-repeat',backgroundAttachment:'fixed',backgroundPosition:'center',backgroundSize:'cover'}:{display:'none'}}>
        <div style={{width:'150px',height:'150px',borderRadius:'50%',backgroundColor:'white',display:'flex',alignItems:'center',justifyContent:'center'}}>
          <img src='https://cdn-icons-png.flaticon.com/512/5556/5556468.png' style={{width:"80%"}}></img>
          
        </div>
        <h3 style={{fontFamily:'monospace',fontSize:'22px',color:'white',paddingLeft:'5px'}}>Admin</h3>
        <br></br>
        <div style={{width:'auto',display:'flex',alignItems:'center',justifyContent:'space-evenly'}}>
        <input id='pass' type='password' autoComplete='off' placeholder='Enter Password' style={{width:'200px',height:'30px',margin:'20px',borderRadius:'10px',border:'none',outline:'none',textAlign:'center',fontFamily:'monospace',fontSize:'12px',backgroundColor:'gray'}}></input>
        <div style={{backgroundColor:'white',width:'35px',height:'35px',borderRadius:'50%',cursor:'pointer'}} onClick={unlock}>
          <img src='https://cdn-icons-png.flaticon.com/512/891/891373.png' style={{width:'70%',height:'70%',borderRadius:'0%',marginLeft:'10%',marginTop:'12%'}}></img>

        </div>
        </div>
    </div>
    <div style={(islocked)?{display:'none'}:{display:'flex',flexDirection:'column',justifyContent:'space-between',alignItems:'center',backgroundImage:`url(${backlock})`,width:'100vw',height:'100vh',backgroundRepeat:'no-repeat',backgroundAttachment:'fixed',backgroundPosition:'center',backgroundSize:'cover'}}>
      <Nav windows={[...windows]} setwindows={setwindows} setscreenopen={setscreenopen} setname={setname} />
      <Body windows={[...windows]} setwindows={setwindows} screenopen={screenopen} setname={setname} setscreenopen={setscreenopen}/>
      <Taskbar instpassed={instpassed} setinstpassed={setinstpassed} issim={issim} setissim={setissim} terminalz={terminalz} setterminalz={setterminalz} windows={[...windows]} setwindows={setwindows} />
      {/* <div style={{width:'100vw',position:'absolute',top:'0',left:'0',height:'100vh',overflow:'hidden',zIndex:'0'}}> */}
      {
      windows.map((window)=>(
        <div key={window.heading}>
        <Rnd
      default={{
        x: 220,
        y: 80,
        width: 650,
        height: 450
      }}
      minHeight={450}
      minWidth={650}
      disableDragging={isDragging}
      
      style={(window.state)?{zIndex:`${window.zi}`,backgroundColor:'#202121',borderRadius:'10px'}:{width:'0px',height:'0px',zIndex:'-100',marginTop:'100vh',visibility:'hidden',transition:'all 0.4s ease-in-out'}}
    >
    <Simulationwindow instpassed={instpassed} setinstpassed={setinstpassed} issim={issim} setissim={setissim} terminalz={terminalz} screenopen={screenopen} setname={setname} setscreenopen={setscreenopen} isDragging={isDragging} setIsDragging={setIsDragging}  windows={[...windows]} setwindows={setwindows} opt={window}></Simulationwindow>
    </Rnd>
    </div>
      ))
      
    }
    {/* </div> */}
      
    </div>
    </div>
  );
}

export default App;
