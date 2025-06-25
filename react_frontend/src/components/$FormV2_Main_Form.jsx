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
            <div className={"section"}>
                <div className={"column"}>
                    <div className={"row"}>
                        <label>Type</label><input type="text" name="Type" onChange={handleChange} required />
                    </div>
                    <div className={"row"}>
                        <label>Due Date</label><input type="text" name="Due Date" onChange={handleChange} required />
                    </div>
                    <div className={"row"}>
                        <label>Status</label><input type="text" name="Status" onChange={handleChange} required />
                    </div>
                    <div className={"row"}>
                        <label>Related Project</label><input type="text" name="Related Project" onChange={handleChange} required />
                    </div>
                    <div className={"row"}>
                        <label>Project Name</label><input type="text" name="Project Name" onChange={handleChange} required />
                    </div>
                </div>
            </div>

            <button type="submit">Submit</button>
        </form>
    );
};

export default $FormV2_Main_Form;
