import json
import os

# Set output directory for React components
output_dir = "react_frontend/src/components/"
api_url = "http://localhost:5000/api"

# Load JSON structure
with open("simple_app_qbl.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

def generate_inputs(field, field_type):
    input_elements = ""
    # Determine input restrictions
    if field_type == "Number":
        validation_logic += f"if (isNaN(formData.{field})) {{ alert('{field} must be a number!'); return; }}\n"
        input_elements += f'<label>{field}</label><input type="number" name="{field}" onChange={{handleChange}} required/>\n\t\t\t'
    elif field_type == "Text":
        input_elements += f'<label>{field}</label><input type="text" name="{field}" onChange={{handleChange}} required/>\n\t\t\t'
    elif field_type == "Boolean":
        input_elements += f'<label>{field}</label><input type="checkbox" name="{field}" onChange={{handleChange}}/>\n\t\t\t'
    else:
        input_elements += f'<label>{field}</label><input type="text" name="{field}" onChange={{handleChange}} required/>\n\t\t\t'
    return input_elements

def generate_v2_form_component(form_name, form_data, field_map):
    print('generate_v2_form_component')
    print('field_map')
    # print(field_map)
    """ Generates a React form with validation based on input rules. """
    
    pages = form_data.get("Pages", {})
    rules = form_data.get("Rules", {})

    validation_logic = ""
    input_elements = ""

    for page, page_props in pages.items():
        print(page)
        # print(page_props)
        sections = page_props.get("Sections", {})
        for section, section_props in sections.items():
            input_elements += "<div className={\"section\"}>\n\t\t\t"
            print(section)
            # print(section_props)
            columns = section_props.get("Columns", {})
            for column, column_props in columns.items():
                input_elements += "<div className={\"column\"}>\n\t\t\t"
                print(column)
                # print(section_props)
                fields = column_props.get("Elements", {})
                for field, field_props in fields.items():
                    print(field)
                    print(field_props)
                    field_type = field_props.get("Type", "text")  # Default to text if type is missing

                    # if "Elements" in field_props:
                    #     input_elements += "<div className={\"row\"}>\n\t\t\t"
                    #     for field, field_props in field_props["Elements"].items():
                    #         field_name = field_map[field_props['Properties']['Field']['Field']]
                    #         field_type = field_props.get("Type", "text")  # Default to text if type is missing
                    #         input_elements += generate_inputs(field_name['Properties']['Label'], field_type)
                    #     input_elements += "</div>\t\t\t"
                    # else:
                    #     print('field name')
                    #     print(field_props['Properties']['Field']['Field'])
                    if field_props["Type"] == "QB::FormV2::Element::Field":
                        field_name = field_map[field_props['Properties']['Field']['Field']]
                        input_elements += "<div className={\"row\"}>\n\t\t\t"
                        input_elements += generate_inputs(field_name['Properties']['Label'], field_type)
                        input_elements += "</div>\n\t\t\t"
                input_elements += "</div>\n\t\t\t"
            input_elements += "</div>\n\t\t\t"

    print('input_elements')
    print(input_elements)

        

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

def generate_form_component(form_name, form_data, field_map):
    print('field_map')
    # print(field_map)
    """ Generates a React form with validation based on input rules. """
    fields = form_data.get("Elements", {})
    rules = form_data.get("Rules", {})

    validation_logic = ""
    input_elements = ""

    for field, field_props in fields.items():
        field_type = field_props.get("Type", "text")  # Default to text if type is missing

        if "Elements" in field_props:
            input_elements += "<div className={\"row\"}>\n\t\t\t"
            for field, field_props in field_props["Elements"].items():
                field_name = field_map[field_props['Properties']['Field']['Field']]
                field_type = field_props.get("Type", "text")  # Default to text if type is missing
                input_elements += generate_inputs(field_name['Properties']['Label'], field_type)
            input_elements += "</div>\t\t\t"
        else:
            print('field name')
            print(field_props['Properties']['Field']['Field'])
            field_name = field_map[field_props['Properties']['Field']['Field']]
            input_elements += "<div className={\"row\"}>\n\t\t\t"
            input_elements += generate_inputs(field_name['Properties']['Label'], field_type)
            input_elements += "</div>\n\t\t\t"

        

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
            <h2>{table_data['Properties']['Name']}</h2>
            <table>
                <thead>
                    <tr>
                        {"".join([f"<th>{reports[col]['Properties']['Name']}</th>" for col in reports.keys()])}
                    </tr>
                </thead>
                <tbody>
                    {{data.map((row, index) => (
                        <tr key={{index}}>
                            {"".join([f"<td><a href=\"./reports/{reports[col]['Id']}\">{reports[col]['Properties']['Name']}</a></td>" for col in reports.keys()])}
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
# generate_api_service()

# print('checking data')
# print(data.get("Resources", {}).get("$App_Simple_App", {}).get("Tables", {}).items())
# print(data.get("Resources", {}).get("$App_Project_Hub", {}).get("Dashboards", {}).items())

# Generate components for tables, dashboards, and forms
for table_name, table_data in data.get("Resources", {}).get("$App_Simple_App", {}).get("Tables", {}).items():
    generate_table_component(table_name, table_data)

for dashboard_name, dashboard_data in data.get("Resources", {}).get("$App_Simple_App", {}).get("Dashboards", {}).items():
    generate_dashboard_component(dashboard_name, dashboard_data)

project_fields = data.get("Resources", {}).get("$App_Simple_App", {}).get("Tables", {}).get("$Table_Project", {}).get("Fields", {})
for form_name, form_data in data.get("Resources", {}).get("$App_Simple_App", {}).get("Tables", {}).get("$Table_Project", {}).get("Forms", {}).get("Resources", {}).items():
    if form_data["Type"] == "QB::FormV2":
        generate_v2_form_component(form_name, form_data, project_fields)
    else:
        generate_form_component(form_name, form_data, project_fields)

task_fields = data.get("Resources", {}).get("$App_Simple_App", {}).get("Tables", {}).get("$Table_Tasks", {}).get("Fields", {})
for form_name, form_data in data.get("Resources", {}).get("$App_Simple_App", {}).get("Tables", {}).get("$Table_Tasks", {}).get("Forms", {}).get("Resources", {}).items():
    if form_data["Type"] == "QB::FormV2":
        generate_v2_form_component(form_name, form_data, task_fields)
    else:
        generate_form_component(form_name, form_data, task_fields)

print("React components successfully generated!")