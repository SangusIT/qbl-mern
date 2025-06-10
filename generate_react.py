import json
import os

# Set output directory for React components
output_dir = "react_frontend/src/components/"
api_url = "http://localhost:5000/api"

# Load JSON structure
with open("sample_qbl.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

def generate_form_component(form_name, form_data):
    """ Generates a React form with validation based on input rules. """
    fields = form_data.get("Fields", {})
    rules = form_data.get("Rules", {})

    validation_logic = ""
    input_elements = ""

    for field, field_props in fields.items():
        field_type = field_props.get("Type", "text")  # Default to text if type is missing

        # Determine input restrictions
        if field_type == "Number":
            validation_logic += f"if (isNaN(formData.{field})) {{ alert('{field} must be a number!'); return; }}\n"
            input_elements += f'<label>{field}<input type="number" name="{field}" onChange={{handleChange}} required/></label><br/>'
        elif field_type == "Text":
            input_elements += f'<label>{field}<input type="text" name="{field}" onChange={{handleChange}} required/></label><br/>'
        elif field_type == "Boolean":
            input_elements += f'<label>{field}<input type="checkbox" name="{field}" onChange={{handleChange}}/></label><br/>'
        else:
            input_elements += f'<label>{field}<input type="text" name="{field}" onChange={{handleChange}} required/></label><br/>'

    component_code = f"""import React, {{ useState }} from 'react';
import {{ createRecord }} from '../apiService';

const {form_name} = () => {{
    const [formData, setFormData] = useState({{}});

    const handleChange = (e) => {{
        setFormData({{ ...formData, [e.target.name]: e.target.value }});
    }};

    const handleSubmit = (e) => {{
        e.preventDefault();
        {validation_logic}
        createRecord('{form_name}', formData);
    }};

    return (
        <form onSubmit={{handleSubmit}}>
            <h2>{form_name}</h2>
            {input_elements}
            <button type="submit">Submit</button>
        </form>
    );
}};

export default {form_name};
    """
    create_component(form_name, component_code)

def create_component(name, content):
    """ Saves a generated React component. """
    filename = os.path.join(output_dir, f"{name}.jsx")
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Created {filename}")

def generate_api_service():
    """ Generates API service file for backend communication. """
    service_code = """import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

export const fetchData = async (endpoint) => {
    try {
        const response = await axios.get(`${API_URL}/${endpoint}`);
        return response.data;
    } catch (error) {
        console.error('API Error:', error);
        return null;
    }
};

export const createRecord = async (endpoint, data) => {
    try {
        const response = await axios.post(`${API_URL}/${endpoint}`, data);
        return response.data;
    } catch (error) {
        console.error('API Error:', error);
        return null;
    }
};

export const updateRecord = async (endpoint, id, data) => {
    try {
        const response = await axios.put(`${API_URL}/${endpoint}/${id}`, data);
        return response.data;
    } catch (error) {
        console.error('API Error:', error);
        return null;
    }
};

export const deleteRecord = async (endpoint, id) => {
    try {
        await axios.delete(`${API_URL}/${endpoint}/${id}`);
    } catch (error) {
        console.error('API Error:', error);
    }
};    

export default { fetchData, createRecord, updateRecord, deleteRecord };
    """
    create_component("apiService", service_code)

def generate_table_component(table_name, table_data):
    """ Generates a React table component with API calls. """
    reports = table_data.get("Reports", {})
    
    component_code = f"""import React, {{ useEffect, useState }} from 'react';
import {{ fetchData }} from '../apiService';

const {table_name} = () => {{
    const [data, setData] = useState([]);

    useEffect(() => {{
        fetchData('{table_name}').then((result) => setData(result));
    }}, []);

    return (
        <div>
            <h2>{table_name}</h2>
            <table>
                <thead>
                    <tr>
                        {"".join([f"<th>{col}</th>" for col in reports.keys()])}
                    </tr>
                </thead>
                <tbody>
                    {{data.map((row, index) => (
                        <tr key={index}>
                            {"".join([f"<td>{{{{row.{col}}}}}</td>" for col in reports.keys()])}
                        </tr>
                    ))}}
                </tbody>
            </table>
        </div>
    );
}};

export default {table_name};
    """
    create_component(table_name, component_code)

def generate_dashboard_component(dashboard_name, dashboard_data):
    """ Generates a React dashboard component with interactive tabs. """
    tabs = dashboard_data.get("Tabs", {}).keys()

    component_code = f"""import React from 'react';

const {dashboard_name} = () => {{
    return (
        <div>
            <h2>{dashboard_name}</h2>
            <ul>
                {"".join([f"<li>{tab}</li>" for tab in tabs])}
            </ul>
        </div>
    );
}};

export default {dashboard_name};
    """
    create_component(dashboard_name, component_code)

# Generate API service
generate_api_service()

# Generate components for tables, dashboards, and forms
for table_name, table_data in data.get("QuickBaseApp", {}).get("Tables", {}).items():
    generate_table_component(table_name, table_data)

for dashboard_name, dashboard_data in data.get("QuickBaseApp", {}).get("Dashboards", {}).items():
    generate_dashboard_component(dashboard_name, dashboard_data)

for form_name, form_data in data.get("QuickBaseApp", {}).get("Forms", {}).items():
    generate_form_component(form_name, form_data)

print("React components successfully generated!")