import React, { useEffect, useState } from 'react';
import { fetchData } from '../apiService';

const $Table_Tasks = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetchData('$Table_Tasks').then((result) => setData(result));
    }, []);

    return (
        <div>
            <h2>$Table_Tasks</h2>
            <table>
                <thead>
                    <tr>
                        <th>$Report_Embedded_for_Project</th><th>$Report_List_All</th><th>$Report_List_Changes</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map((row, index) => (
                        <tr key={index}>
                            <td>{{row.$Report_Embedded_for_Project}}</td><td>{{row.$Report_List_All}}</td><td>{{row.$Report_List_Changes}}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default $Table_Tasks;
    