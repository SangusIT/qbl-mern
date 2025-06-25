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
            <div className={"row"}>
			<label>Type</label><input type="text" name="Type" onChange={handleChange} required/>
			</div>
			<div className={"row"}>
			<label>Due Date</label><input type="text" name="Due Date" onChange={handleChange} required/>
			</div>
			<div className={"row"}>
			<label>Status</label><input type="text" name="Status" onChange={handleChange} required/>
			</div>
			<div className={"row"}>
			<label>Project Name</label><input type="text" name="Project Name" onChange={handleChange} required/>
			</div>
			
            <button type="submit">Submit</button>
        </form>
    );
};

export default $Form_Tasks_Main_Form;
    