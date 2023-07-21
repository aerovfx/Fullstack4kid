// class component

// function component
import React from 'react';
import FormComponent from './FormComponent';
import MySecondComponent from './MySecondComponent';
import DisplayInfoComponent from './DisplayInfoComponent';
class MyComponent extends React.Component {
    render (){
        // truyen doi tuong, bien
        // const myAge = 50;
        let person = {
            name: "Noname",
            address: "Nowhere",
            age: 100
        }
        return (
            <div>
                My first component
                <hr/>
                <MySecondComponent />
                <hr/>
                <FormComponent />
                <hr/>
                <DisplayInfoComponent name = {person.name} age = {person.age} address = {person.address}/>
            </div>
        );

    }
}
export default MyComponent;