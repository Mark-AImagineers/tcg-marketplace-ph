import { useState, useContext } from 'react';
import { AuthContext } from '../auth/AuthContext';
import client from '../api/client';

export default function Login() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const { setUser } = useContext(AuthContext);

    async function handleSubmit(e) {
        e.preventDefault();

        const formData = new URLSearchParams();
        formData.append('username', email);
        formData.append('password', password);

        try {
            const res = await client.post('/api/users/login', formData);
            console.log('Login success:', res.data);

            //replace with /me later
            setUser({ email });
        } catch (err) {
            console.error('Login failed:', err.response?.data || err.message);
        }
    }

    return (
        <div>
            <h1>Login</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="email">Email:</label><br />
                <input
                    type="email"
                    id="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                /><br />

                <label htmlFor="password">Password:</label><br />
                <input
                    type="password"
                    id="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                /><br />

                <button type="submit">Login</button>
            </form>
        </div>
    );
}