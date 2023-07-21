// class component

// function component
import React from 'react';

class DisplayInfoComponent extends React.Component {
    render (){
        console.log(this.props)
        //Props truyen data 
        // tu Component cha la MyComponent 
        // xuong component con la DisplayInfoComponent
        return (
            <div>
               
                <div>My name's {this.props.name}</div>
                <div>My address's {this.props.address}</div>
                <div>My age's {this.props.age}</div>
        
            </div>
        );

    }
}
export default DisplayInfoComponent;