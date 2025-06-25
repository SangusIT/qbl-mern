import React, { useEffect, useState } from 'react';
import { fetchData } from '../apiService';

const $Table_Tasks = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetchData('$Table_Tasks').then((result) => setData(result));
    }, []);

    return (
        <div>
            <h2>Tasks</h2>
            <table>
                <thead>
                    <tr>
                        <th>Embedded for Project</th><th>List All</th><th>List Changes</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map((row, index) => (
                        <tr key={index}>
                            <td><a href="./reports/5">Embedded for Project</a></td><td><a href="./reports/1">List All</a></td><td><a href="./reports/2">List Changes</a></td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default $Table_Tasks;
    