let scene, camera, renderer, world;
const balls = [];
const MAX_BALLS = 5;

function init() {
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById('scene-container').appendChild(renderer.domElement);

    world = new CANNON.World();
    world.gravity.set(0, -0.1, 0);

    camera.position.z = 10;  // Increased camera distance for better visibility

    const light = new THREE.PointLight(0xffffff, 1, 100);
    light.position.set(0, 0, 10);
    scene.add(light);

    // Add ambient light for better visibility
    const ambientLight = new THREE.AmbientLight(0x404040);
    scene.add(ambientLight);

    setInterval(addBall, 1000);
    animate();
}

function addBall() {
    if (balls.length >= MAX_BALLS) {
        const oldestBall = balls.shift();
        scene.remove(oldestBall.mesh);
        world.removeBody(oldestBall.body);
    }

    fetch('/cpu_usage')
        .then(response => response.json())
        .then(data => {
            const radius = 0.3 + (data.cpu_usage / 100) * 0.7;
            const ballShape = new CANNON.Sphere(radius);
            const ballBody = new CANNON.Body({
                mass: 1,
                shape: ballShape,
            });
            ballBody.position.set(
                Math.random() * 8 - 4,
                Math.random() * 8 + 4,
                Math.random() * 8 - 4
            );
            world.addBody(ballBody);

            const ballGeometry = new THREE.SphereGeometry(radius, 32, 32);
            const ballMaterial = new THREE.MeshPhongMaterial({ 
                color: Math.random() * 0xffffff,
                shininess: 100
            });
            const ballMesh = new THREE.Mesh(ballGeometry, ballMaterial);
            scene.add(ballMesh);

            balls.push({ body: ballBody, mesh: ballMesh });
        });
}

function animate() {
    requestAnimationFrame(animate);
    world.step(1 / 60);
    balls.forEach(ball => {
        ball.mesh.position.copy(ball.body.position);
        ball.mesh.quaternion.copy(ball.body.quaternion);
    });
    renderer.render(scene, camera);
}

window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

init();
