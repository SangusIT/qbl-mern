import React, { useState } from 'react';
import { createRecord } from '../apiService';

const $FormV2_Main_Form = () => {
    const [formData, setFormData] = useState({});

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        
        createRecord('$FormV2_Main_Form', formData);
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>$FormV2_Main_Form</h2>
            
            <button type="submit">Submit</button>
        </form>
    );
};

export default $FormV2_Main_Form;
    