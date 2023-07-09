import React from "react";

class VComponent extends React.Component {
    state = {
        name: 'Viet Chung',
        old: '36'
    }
    handleClick(){
        console.log(">>click my button")
    }

    render () {
        return (
            <div>Hello,
            My name is {this.state.name}, {this.state.old}<br/>
            <button onClick={this.handleClick}>Click me</button>
            </div>
        )
    }
}
export default VComponent;
