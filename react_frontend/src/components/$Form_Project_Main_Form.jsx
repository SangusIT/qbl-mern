import React, { useState } from 'react';
import { createRecord } from '../apiService';

const $Form_Project_Main_Form = () => {
    const [formData, setFormData] = useState({});

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        createRecord('$Form_Project_Main_Form', formData);
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>$Form_Project_Main_Form</h2>
            <div className={"row"}>
                <label>Project Name</label><input type="text" name="Project Name" onChange={handleChange} required />
            </div>
            <div className={"row"}>
                <label>Add Task</label><input type="text" name="Add Task" onChange={handleChange} required />
                <label>Task records</label><input type="text" name="Task records" onChange={handleChange} required />
                <label># of Completed Tasks</label><input type="text" name="# of Completed Tasks" onChange={handleChange} required />
                <label># of Tasks</label><input type="text" name="# of Tasks" onChange={handleChange} required />
            </div>
            <button type="submit">Submit</button>
        </form>
    );
};

export default $Form_Project_Main_Form;
