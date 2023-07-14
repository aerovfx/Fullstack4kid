// class component

// function component
import React from "react";
import UserInfor from './UserInfor';
import Displayinfo from "./Displayinfor";


class MyComponent  extends React.Component {
 
    render() {
        const myInfo = ['ab', 'ds']
    
        //console.log(this.props)
        return (
            <div>
               <UserInfor />
               <hr/>
               <Displayinfo name = "VietChung" yo="20"/>
               <hr/>
               <Displayinfo name={"Nhanma"} yo ={36} myInfo={myInfo}/>

            </div>
        );
    }


}
export default MyComponent;