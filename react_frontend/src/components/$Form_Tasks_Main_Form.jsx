import React, { useState } from 'react';
import { createRecord } from '../apiService';

const $Form_Tasks_Main_Form = () => {
    const [formData, setFormData] = useState({});

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        
        createRecord('$Form_Tasks_Main_Form', formData);
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>$Form_Tasks_Main_Form</h2>
            <label>$FormElement_1<input type="text" name="$FormElement_1" onChange={handleChange} required/></label><br/><label>$FormElement_2<input type="text" name="$FormElement_2" onChange={handleChange} required/></label><br/><label>$FormElement_3<input type="text" name="$FormElement_3" onChange={handleChange} required/></label><br/><label>$FormElement_4<input type="text" name="$FormElement_4" onChange={handleChange} required/></label><br/>
            <button type="submit">Submit</button>
        </form>
    );
};

export default $Form_Tasks_Main_Form;
    