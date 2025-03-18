from collections import deque

def bfs_shortest_path(city_map, start, goal):
    queue = deque([(start, [start])])  # (lokasi_saat_ini, jalur_ke_lokasi)
    visited = set()

    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path  # Kembalikan rute terpendek jika tujuan ditemukan
        if current not in visited:
            visited.add(current)
            for neighbor in city_map.get(current, []):
                queue.append((neighbor, path + [neighbor]))
    
    return None  # Kembalikan None jika tidak ada jalur

# Contoh penggunaan
city_map = {
    'Rumah': ['Mall', 'Sekolah'],
    'Mall': ['Gym', 'Rumah Sakit'],
    'Sekolah': ['Perpustakaan'],
    'Gym': ['Rumah Sakit'],
    'Perpustakaan': ['Rumah Sakit'],
    'Rumah Sakit': []
}

start = 'Rumah'
goal = 'Rumah Sakit'
shortest_path = bfs_shortest_path(city_map, start, goal)
print("Rute Terpendek:", shortest_path)
