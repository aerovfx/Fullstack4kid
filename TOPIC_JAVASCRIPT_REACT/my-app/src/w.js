<BrowserRouter>
        <Box sx = {{ backgroundColor: '#000'}}>
            <Navbar />
            <h1>hi!</h1>
            <Routes>
                <Route path ='/' extract element={<Feed />} />
                <Route path ='/video/:id' element={<VideoDetail />} />
                <Route path ='/channel/:id' element={<ChannelDetail />} />
                <Route path ='/search/:searchTerm' element={<SearchFeed />} />
            </Routes>
        </Box>
    </BrowserRouter>