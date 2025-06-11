import axios from 'axios';

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
    